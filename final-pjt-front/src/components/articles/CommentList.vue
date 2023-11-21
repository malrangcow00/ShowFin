<template>
  <div>
    <h3>댓글 목록</h3>
    <div v-if="comments && comments.length > 0">
      <CommentListItem
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
      />
    </div>
  </div>
</template>

<script setup>
import CommentListItem from "@/components/articles/CommentListItem.vue";

defineProps({
  comments: Object,
});
</script>

<style scoped></style>
