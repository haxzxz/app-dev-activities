from blog.models import Post, Comment

post1 = Post.objects.create(title="My FIrst Post",content="Hello PUP",author="Christian")
post2 = Post.objects.create(title="Second Post Using Django Create",content="Hello App-Dev",author="Christian")
comment1 = Comment.objects.create(post=post1,text="Nice First Post!",commenter="Abel")
comment2 = Comment.objects.create(post=post2,text="Good Day App-Dev Classmates",commenter="Drake")

all_post = Post.objects.all()
print(all_post)

print(post1.title, post1.author)

post1.title = "Updated Post Title"
post1.save()

comment1.delete()

christian_posts = Post.objects.filter(author="Christian")

comments_on_post = post1.comments.all()