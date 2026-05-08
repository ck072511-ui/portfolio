<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Advanced Library Management System</title>
<style>
  *{box-sizing:border-box;margin:0;padding:0;}
  body{font-family:"Poppins",sans-serif;display:flex;background:#f4f6f9;color:#333;}
  /* Sidebar */
  .sidebar{width:250px;background:#1e293b;height:100vh;position:fixed;left:0;top:0;color:white;display:flex;flex-direction:column;padding-top:1.5rem;}
  .sidebar h2{text-align:center;margin-bottom:2rem;font-size:1.5rem;}
  .sidebar a{color:white;text-decoration:none;padding:1rem;text-align:center;transition:0.3s;}
  .sidebar a:hover{background:#334155;}
  /* Main Section */
  main{margin-left:250px;flex-grow:1;padding:2rem;}
  header{font-size:1.8rem;font-weight:600;margin-bottom:1rem;color:#0078d7;}
  .card{background:white;padding:1.5rem;border-radius:12px;box-shadow:0 4px 10px rgba(0,0,0,0.1);margin-bottom:2rem;}
  .dashboard-cards{display:flex;gap:1rem;flex-wrap:wrap;}
  .dashboard-card{flex:1 1 200px;background:#0078d7;color:white;padding:1rem;border-radius:10px;text-align:center;}
  .dashboard-card h3{margin-bottom:0.5rem;}
  form{display:flex;flex-wrap:wrap;gap:1rem;margin-top:1rem;}
  form input, form select{flex:1 1 45%;padding:0.6rem;border:1px solid #ccc;border-radius:6px;font-size:1rem;}
  form button{flex:1 1 100%;padding:0.75rem;background-color:#0078d7;color:white;border:none;border-radius:6px;cursor:pointer;font-size:1rem;}
  form button:hover{background-color:#005fa3;}
  #searchBar{width:100%;padding:0.6rem;margin-bottom:1rem;border-radius:6px;border:1px solid #ccc;font-size:1rem;}
  table{width:100%;border-collapse:collapse;margin-top:1rem;}
  th,td{border:1px solid #ddd;padding:0.75rem;text-align:center;}
  th{background-color:#0078d7;color:white;}
  tr:nth-child(even){background-color:#f9f9f9;}
  .btn{padding:0.3rem 0.7rem;border:none;border-radius:4px;cursor:pointer;}
  .delete-btn{background-color:#ff5252;color:white;}
  .delete-btn:hover{background-color:#e60000;}
  .edit-btn{background-color:#00b894;color:white;}
  .edit-btn:hover{background-color:#009970;}
  @media(max-width:768px){.sidebar{display:none;} main{margin:0;padding:1rem;}}
</style>
</head>
<body>

<div class="sidebar">
  <h2>📚 Library</h2>
  <a href="#" onclick="showSection('dashboard')">Dashboard</a>
  <a href="#" onclick="showSection('books')">Books</a>
  <a href="#" onclick="showSection('members')">Members</a>
  <a href="#" onclick="showSection('issues')">Issue/Return</a>
</div>

<main>
  <header>Advanced Library Management System</header>

  <!-- Dashboard -->
  <div id="dashboard" class="card section">
    <h3>Dashboard</h3>
    <div class="dashboard-cards">
      <div class="dashboard-card">
        <h3>Total Books</h3>
        <p id="totalBooks">0</p>
      </div>
      <div class="dashboard-card">
        <h3>Total Members</h3>
        <p id="totalMembers">0</p>
      </div>
      <div class="dashboard-card">
        <h3>Issued Books</h3>
        <p id="totalIssued">0</p>
      </div>
    </div>
  </div>

  <!-- Books Section -->
  <div id="books" class="card section" style="display:none">
    <h3>Add/Edit Book</h3>
    <form id="bookForm">
      <input type="hidden" id="bookEditIndex" value="">
      <input type="text" id="bookTitle" placeholder="Book Title" required>
      <input type="text" id="bookAuthor" placeholder="Author Name" required>
      <input type="text" id="bookISBN" placeholder="ISBN" required>
      <button type="submit">Save Book</button>
    </form>
    <input type="text" id="bookSearch" placeholder="Search by Title or Author...">
    <table id="bookTable">
      <thead>
        <tr><th>#</th><th>Title</th><th>Author</th><th>ISBN</th><th>Actions</th></tr>
      </thead>
      <tbody></tbody>
    </table>
  </div>

  <!-- Members Section -->
  <div id="members" class="card section" style="display:none">
    <h3>Add/Edit Member</h3>
    <form id="memberForm">
      <input type="hidden" id="memberEditIndex" value="">
      <input type="text" id="memberName" placeholder="Member Name" required>
      <input type="text" id="memberEmail" placeholder="Member Email" required>
      <button type="submit">Save Member</button>
    </form>
    <input type="text" id="memberSearch" placeholder="Search by Name or Email...">
    <table id="memberTable">
      <thead>
        <tr><th>#</th><th>Name</th><th>Email</th><th>Actions</th></tr>
      </thead>
      <tbody></tbody>
    </table>
  </div>

  <!-- Issue/Return Section -->
  <div id="issues" class="card section" style="display:none">
    <h3>Issue/Return Books</h3>
    <form id="issueForm">
      <select id="issueBook" required></select>
      <select id="issueMember" required></select>
      <button type="submit">Issue Book</button>
    </form>
    <table id="issueTable">
      <thead>
        <tr><th>#</th><th>Book</th><th>Member</th><th>Date</th><th>Actions</th></tr>
      </thead>
      <tbody></tbody>
    </table>
  </div>

</main>

<script>
let books = JSON.parse(localStorage.getItem("books"))||[];
let members = JSON.parse(localStorage.getItem("members"))||[];
let issues = JSON.parse(localStorage.getItem("issues"))||[];

function saveData(){localStorage.setItem("books",JSON.stringify(books));
localStorage.setItem("members",JSON.stringify(members));
localStorage.setItem("issues",JSON.stringify(issues));updateDashboard();}

function showSection(section){document.querySelectorAll('.section').forEach(s=>s.style.display='none');document.getElementById(section).style.display='block';displayBooks();displayMembers();displayIssues();}

function updateDashboard(){document.getElementById("totalBooks").innerText=books.length;document.getElementById("totalMembers").innerText=members.length;document.getElementById("totalIssued").innerText=issues.length;}

function displayBooks(filter=""){const tbody=document.querySelector("#bookTable tbody");tbody.innerHTML="";const filtered=books.filter(b=>b.title.toLowerCase().includes(filter.toLowerCase())||b.author.toLowerCase().includes(filter.toLowerCase()));filtered.forEach((b,i)=>{const tr=document.createElement("tr");tr.innerHTML=<td>${i+1}</td><td>${b.title}</td><td>${b.author}</td><td>${b.isbn}</td><td><button class="btn edit-btn" onclick="editBook(${i})">Edit</button> <button class="btn delete-btn" onclick="deleteBook(${i})">Delete</button></td>;tbody.appendChild(tr);});updateIssueBookOptions();}

function displayMembers(filter=""){const tbody=document.querySelector("#memberTable tbody");tbody.innerHTML="";const filtered=members.filter(m=>m.name.toLowerCase().includes(filter.toLowerCase())||m.email.toLowerCase().includes(filter.toLowerCase()));filtered.forEach((m,i)=>{const tr=document.createElement("tr");tr.innerHTML=<td>${i+1}</td><td>${m.name}</td><td>${m.email}</td><td><button class="btn edit-btn" onclick="editMember(${i})">Edit</button> <button class="btn delete-btn" onclick="deleteMember(${i})">Delete</button></td>;tbody.appendChild(tr);});updateIssueMemberOptions();}

function displayIssues(){const tbody=document.querySelector("#issueTable tbody");tbody.innerHTML="";issues.forEach((i,index)=>{const tr=document.createElement("tr");tr.innerHTML=<td>${index+1}</td><td>${i.book}</td><td>${i.member}</td><td>${i.date}</td><td><button class="btn delete-btn" onclick="returnBook(${index})">Return</button></td>;tbody.appendChild(tr);});}

function editBook(index){const b=books[index];document.getElementById("bookTitle").value=b.title;document.getElementById("bookAuthor").value=b.author;document.getElementById("bookISBN").value=b.isbn;document.getElementById("bookEditIndex").value=index;}
function deleteBook(index){if(confirm("Delete this book?")){books.splice(index,1);saveData();displayBooks();}}
function editMember(index){const m=members[index];document.getElementById("memberName").value=m.name;document.getElementById("memberEmail").value=m.email;document.getElementById("memberEditIndex").value=index;}
function deleteMember(index){if(confirm("Delete this member?")){members.splice(index,1);saveData();displayMembers();}}

function returnBook(index){if(confirm("Return this book?")){issues.splice(index,1);saveData();displayIssues();}}

document.getElementById("bookForm").addEventListener("submit",e=>{e.preventDefault();const title=document.getElementById("bookTitle").value.trim();const author=document.getElementById("bookAuthor").value.trim();const isbn=document.getElementById("bookISBN").value.trim();const editIndex=document.getElementById("bookEditIndex").value;if(editIndex===""){books.push({title,author,isbn});}else{books[editIndex]={title,author,isbn};document.getElementById("bookEditIndex").value="";}saveData();displayBooks();e.target.reset();});

document.getElementById("memberForm").addEventListener("submit",e=>{e.preventDefault();const name=document.getElementById("memberName").value.trim();const email=document.getElementById("memberEmail").value.trim();const editIndex=document.getElementById("memberEditIndex").value;if(editIndex===""){members.push({name,email});}else{members[editIndex]={name,email};document.getElementById("memberEditIndex").value="";}saveData();displayMembers();e.target.reset();});

document.getElementById("bookSearch").addEventListener("input",e=>displayBooks(e.target.value));
document.getElementById("memberSearch").addEventListener("input",e=>displayMembers(e.target.value));

function updateIssueBookOptions(){const select=document.getElementById("issueBook");select.innerHTML="";books.forEach(b=>{select.innerHTML+=<option value="${b.title}">${b.title}</option>;});}
function updateIssueMemberOptions(){const select=document.getElementById("issueMember");select.innerHTML="";members.forEach(m=>{select.innerHTML+=<option value="${m.name}">${m.name}</option>;});}

document.getElementById("issueForm").addEventListener("submit",e=>{e.preventDefault();const book=document.getElementById("issueBook").value;const member=document.getElementById("issueMember").value;const date=new Date().toLocaleDateString();issues.push({book,member,date});saveData();displayIssues();});

showSection('dashboard');
</script>

</body>
</html>
