/**
 * KhojDoot Core Application Coordinator
 * Handles navigation, toast alerts, language dropdown interactions, and storage
 * Designed for Gayatri's KhojDoot Frontend
 */

const KhojApp = {
  init() {
    this.setupLanguageDropdown();
    this.highlightActiveNavLink();
    this.setupToasts();
    console.log("KhojDoot Frontend initialized successfully.");
  },

  // Setup language dropdown toggling
  setupLanguageDropdown() {
    const btn = document.getElementById('langDropdownBtn');
    const menu = document.getElementById('langDropdownMenu');

    if (!btn || !menu) return;

    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      menu.classList.toggle('show');
    });

    document.addEventListener('click', (e) => {
      if (!btn.contains(e.target) && !menu.contains(e.target)) {
        menu.classList.remove('show');
      }
    });

    // Option clicks
    const options = menu.querySelectorAll('.lang-option');
    options.forEach(opt => {
      opt.addEventListener('click', () => {
        const lang = opt.getAttribute('data-lang');
        if (lang && typeof KhojLanguage !== 'undefined') {
          KhojLanguage.setLanguage(lang);
          options.forEach(o => o.classList.remove('active'));
          opt.classList.add('active');
          menu.classList.remove('show');
          const toastMsg = KhojLanguage.t('toastLangChanged') || `Language set to ${KhojLanguage.getLanguageName(lang)}`;
          this.showToast(toastMsg, 'info');
        }
      });
    });
  },

  // Highlight active link in the navigation header
  highlightActiveNavLink() {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      const isChatMatch = (currentPath === 'index.html' || currentPath === 'chat.html' || currentPath === '') && (href === 'chat.html' || href === 'index.html');
      if (href && (href === currentPath || isChatMatch)) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  },

  // Toast Notification System
  setupToasts() {
    let container = document.getElementById('toastContainer');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toastContainer';
      container.className = 'toast-container';
      document.body.appendChild(container);
    }
  },

  showToast(message, type = 'info') {
    let container = document.getElementById('toastContainer');
    if (!container) {
      this.setupToasts();
      container = document.getElementById('toastContainer');
    }

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    
    let icon = 'ℹ️';
    if (type === 'success') icon = '✅';
    if (type === 'warning') icon = '⚠️';
    if (type === 'error') icon = '❌';

    toast.innerHTML = `<span>${icon}</span><span>${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => {
        if (toast.parentElement) toast.parentElement.removeChild(toast);
      }, 300);
    }, 3500);
  }
};

document.addEventListener('DOMContentLoaded', () => {
  KhojApp.init();
});
