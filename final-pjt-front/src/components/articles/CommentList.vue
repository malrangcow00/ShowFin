<template>
    <v-row justify="center">
        <v-col max-width="100%">
            <v-card class="pa-8">
                <v-card-title>
                    <h3 class="text-h5 font-weight-bold">댓글 목록</h3>
                </v-card-title>
                <v-divider></v-divider>
                <v-row v-if="comments && comments.length > 0">
                    <CommentListItem
                        v-for="comment in comments"
                        :key="comment.id"
                        :comment="comment"
                    />
                </v-row>
            </v-card>
        </v-col>
    </v-row>
</template>

<script setup>
import CommentListItem from "@/components/articles/CommentListItem.vue";

const props = defineProps({
    comments: Array,
});
</script>

<style scoped>
/* Add any additional styling if needed */
</style>