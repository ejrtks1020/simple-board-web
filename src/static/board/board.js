document.addEventListener('DOMContentLoaded', function() {
  loadPosts();
});

function loadPosts() {
  let posts = JSON.parse(localStorage.getItem('posts')) || [];
  const board = document.getElementById('board');
  posts.forEach(function(content) {
      const post = document.createElement('div');
      post.className = 'post';
      post.textContent = content;
      board.appendChild(post);
  });
}