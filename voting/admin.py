from django.contrib import admin
from .models import Topic, VoteItem

class VoteItemInline(admin.TabularInline):
    model = VoteItem
    extra = 1

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'vote_limit', 'is_unlimited')
    fields = ('name', 'vote_limit', 'is_unlimited')

    inlines = [VoteItemInline]

class VoteItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'votes')
    list_filter = ('topic',)
    search_fields = ('title',)

admin.site.register(Topic, TopicAdmin)
admin.site.register(VoteItem, VoteItemAdmin)