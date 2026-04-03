from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from collections import Counter
from .models import Topic, VoteItem


# 🔹 주제 목록
def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'topic_list.html', {'topics': topics})


# 🔹 주제 상세 (투표 페이지)
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    items = VoteItem.objects.filter(topic=topic)

    return render(request, 'topic_detail.html', {
        'topic': topic,
        'items': items
    })


# 🔹 투표 처리
def vote(request, project_id):
    item = get_object_or_404(VoteItem, id=project_id)
    topic = item.topic

    # ⭐ 현재 주제 총 투표 수 계산
    total_votes = sum(i.votes for i in VoteItem.objects.filter(topic=topic))

    # ⭐ 제한 체크 (무제한이 아닐 때만)
    if not topic.is_unlimited:
        if topic.vote_limit and total_votes >= topic.vote_limit:
            messages.error(request, "투표가 더 이상 불가합니다.")
            return redirect('topic_detail', topic_id=topic.id)

    # 투표 증가
    item.votes += 1
    item.save()

    return redirect('topic_detail', topic_id=topic.id)


# 🔹 결과 페이지 (그래프 + 순위 + 공동순위)
def result(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    # 투표수 기준 정렬
    items = list(VoteItem.objects.filter(topic=topic).order_by('-votes'))

    # ⭐ 동률 체크용
    vote_counts = [item.votes for item in items]
    counter = Counter(vote_counts)

    ranked_items = []
    current_rank = 1
    prev_votes = None

    for index, item in enumerate(items):
        if prev_votes is None:
            rank = 1
        elif item.votes == prev_votes:
            rank = current_rank  # 공동 순위
        else:
            rank = index + 1     # 다음 순위

        ranked_items.append({
            'item': item,
            'rank': rank,
            'count': counter[item.votes]  # 공동 여부 판단
        })

        prev_votes = item.votes
        current_rank = rank

    return render(request, 'result.html', {
        'topic': topic,
        'ranked_items': ranked_items
    })


# 🔹 투표 초기화
def reset_votes(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    items = VoteItem.objects.filter(topic=topic)

    for item in items:
        item.votes = 0
        item.save()

    return redirect('result', topic_id=topic.id)