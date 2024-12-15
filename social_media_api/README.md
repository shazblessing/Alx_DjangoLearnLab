# Social Media API

## Endpoints

### Posts
- `GET /api/posts/posts/`: List all posts.
- `POST /api/posts/posts/`: Create a new post (Authentication required).
- `GET /api/posts/posts/{id}/`: Retrieve a specific post.
- `PUT /api/posts/posts/{id}/`: Update a post (Author only).
- `DELETE /api/posts/posts/{id}/`: Delete a post (Author only).

### Comments
- `GET /api/posts/comments/`: List all comments.
- `POST /api/posts/comments/`: Create a new comment (Authentication required).
- `GET /api/posts/comments/{id}/`: Retrieve a specific comment.
- `PUT /api/posts/comments/{id}/`: Update a comment (Author only).
- `DELETE /api/posts/comments/{id}/`: Delete a comment (Author only).
