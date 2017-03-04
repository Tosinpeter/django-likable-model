# django-likable-model
An abstract model in Django that supports store likes and denormalized like count.

### What is likable model?
If user like a post or a comment. We need to create a *like* table to store who like what,
so that we can avoid the same user contributing too much likes on the same item.

Also in the `Post` or `Comment` model, we need to store a denormalized field `like_count` to
denote how many users liked this item. Why not just select count from like table? Because select count
is heavy, if you store a denormalized field in the model, it's much more faster.

### How to use it?

Say you want to make `Post` model likable.

The orignal model may looks like:

```
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

Change it to:

```
from likable.models import Likable

class Post(Likable):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

When user liked a post:
```
post = Post.objects.get(id=post_id)
post.like_by(user)
```

When user canceled a like:
```
post.like_canceled_by(user)
```

Get how many users liked a post:
```
post.like_count
```

Get most recent likes / users
```
likes = post.get_recent_likes(k=10)
users = [like.user for like in likes]
```
