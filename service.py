from models import PostModel, CommentModel

class BlogService:
    def __init__(self):
        self.post_model = PostModel()
        self.comment_model = CommentModel()

    def create_post(self, title, content):
        return self.post_model.create_post(title, content)

    def update_post(self, post_id, title, content):
        self.post_model.update_post(post_id, title, content)

    def delete_post(self, post_id):
        self.post_model.delete_post(post_id)

    def list_posts(self):
        return self.post_model.list_posts()

    def create_comment(self, post_id, content):
        return self.comment_model.create_comment(post_id, content)

    def list_comments_for_post(self, post_id):
        return self.comment_model.get_comments_by_post(post_id)

    def update_comment(self, comment_id, content):
        self.comment_model.update_comment(comment_id, content)

    def delete_comment(self, comment_id):
        self.comment_model.delete_comment(comment_id)
