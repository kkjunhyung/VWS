from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from collections import Counter
from .models import Topic, VoteItem
import re

# 🔥 유튜브 ID 추출
def get_youtube_id(url):
    if not url:
        return None
    match = re.search(r'v=([^&]+)', url)
    if match:
        return match.group(1)
    match = re.search(r'youtu\.be/([^?&]+)', url)
    if match:
        return match.group(1)
    return None

# 🔹 주제 목록
def topic_list(request):
    topics = Topic.objects.all().order_by('-id')
    return render(request, 'topic_list.html', {'topics': topics})

# 🔹 주제 상세
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    items = VoteItem.objects.filter(topic=topic)

    # 유튜브 ID
    for item in items:
        item.youtube_id = get_youtube_id(item.link)

    total_votes = sum(i.votes for i in items)

    return render(request, 'topic_detail.html', {
        'topic': topic,
        'items': items,
        'total_votes': total_votes
    })

# 🔹 투표 처리
def vote(request, project_id):
    item = get_object_or_404(VoteItem, id=project_id)
    topic = item.topic

    # 유기명 투표면 로그인 필수
    if topic.is_named and not request.user.is_authenticated:
        messages.warning(request, "유기명 투표는 로그인 후 가능합니다.")
        return redirect('login')  # 로그인 페이지로 이동

    total_votes = sum(i.votes for i in VoteItem.objects.filter(topic=topic))

    # 제한 체크
    if not topic.is_unlimited and topic.vote_limit:
        if total_votes >= topic.vote_limit:
            messages.error(request, f"투표 인원이 마감되었습니다 ({total_votes}/{topic.vote_limit})")
            return redirect('topic_detail', topic_id=topic.id)

    # 투표 증가
    item.votes += 1
    item.save()
    total_votes += 1

    messages.success(request, f"투표 완료되었습니다 ({total_votes}/{topic.vote_limit})")

    return redirect('topic_detail', topic_id=topic.id)

# 🔹 결과 페이지
def result(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    items = list(VoteItem.objects.filter(topic=topic).order_by('-votes'))
    vote_counts = [item.votes for item in items]
    counter = Counter(vote_counts)

    ranked_items = []
    current_rank = 1
    prev_votes = None

    for index, item in enumerate(items):
        if prev_votes is None:
            rank = 1
        elif item.votes == prev_votes:
            rank = current_rank
        else:
            rank = index + 1

        ranked_items.append({
            'item': item,
            'rank': rank,
            'count': counter[item.votes]
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

# 🔹 투표 생성
def topic_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        vote_limit = request.POST.get('vote_limit')
        is_unlimited = request.POST.get('is_unlimited') == 'on'
        is_named = request.POST.get('is_named') == 'on'  # 체크박스 값 추가

        if vote_limit:
            vote_limit = int(vote_limit)
            if vote_limit < 1:
                messages.error(request, "투표 제한은 1 이상이어야 합니다.")
                return redirect('topic_create')
        else:
            vote_limit = None

        topic = Topic.objects.create(
            name=title,
            vote_limit=vote_limit,
            is_unlimited=is_unlimited,
            is_named=is_named,  # 유기명 저장
        )

        options = request.POST.getlist('options')
        descriptions = request.POST.getlist('descriptions')
        images = request.FILES.getlist('images')
        links = request.POST.getlist('links')

        for i in range(len(options)):
            if options[i].strip():
                VoteItem.objects.create(
                    topic=topic,
                    title=options[i],
                    description=descriptions[i] if i < len(descriptions) else '',
                    image=images[i] if i < len(images) else None,
                    link=links[i] if i < len(links) else None,
                )

        return redirect('topic_detail', topic_id=topic.id)

    return render(request, 'topic_create.html')

# 🔹 투표 삭제
def topic_delete(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        topic.delete()
    return redirect('topic_list')