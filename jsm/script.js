// Hamburger menu
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));

// Active nav link on scroll
const sections = document.querySelectorAll('section[id], div[id]');
const navItems = document.querySelectorAll('.nav-link');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => {
    if (window.scrollY >= s.offsetTop - 120) current = s.id;
  });
  navItems.forEach(a => {
    a.classList.remove('active');
    if (a.getAttribute('href') === '#' + current) a.classList.add('active');
  });
});

// Enquiry form submit
document.getElementById('enquiryForm').addEventListener('submit', e => {
  e.preventDefault();
  const btn = e.target.querySelector('.btn-submit');
  btn.textContent = '✔ Enquiry Submitted!';
  btn.style.background = '#25d366';
  setTimeout(() => { btn.textContent = 'Submit Enquiry →'; btn.style.background = ''; e.target.reset(); }, 3000);
});

// Navbar shadow on scroll
window.addEventListener('scroll', () => {
  document.getElementById('navbar').style.boxShadow =
    window.scrollY > 10 ? '0 4px 24px rgba(0,0,0,0.13)' : '0 2px 12px rgba(0,0,0,0.08)';
});
