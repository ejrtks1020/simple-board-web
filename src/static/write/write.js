document.getElementById('post-form').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const content = document.getElementById('post-content').value;
  if (content.trim() !== "") {
      savePost(content);
      document.getElementById('post-content').value = '';
      alert("Post saved! You can view it on the board page.");
  }
});

function savePost(content) {
  let posts = JSON.parse(localStorage.getItem('posts')) || [];
  posts.push(content);
  localStorage.setItem('posts', JSON.stringify(posts));
}