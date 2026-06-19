function showToast(message, type = 'success') {
    const container = document.querySelector('.toast-container') || (() => {
        const c = document.createElement('div');
        c.className = 'toast-container';
        document.body.appendChild(c);
        return c;
    })();
    const toast = document.createElement('div');
    toast.className = 'toast-custom mb-3';
    const colors = { success: '#00D2D3', error: '#FF6B6B', warning: '#FECA57', info: '#54A0FF' };
    const icons = { success: 'fa-check-circle', error: 'fa-times-circle', warning: 'fa-exclamation-triangle', info: 'fa-info-circle' };
    toast.innerHTML = <div class="d-flex align-items-center"><span class="me-3" style="color:;font-size:1.2rem;"><i class="fas "></i></span><span class="flex-grow-1"></span><span class="ms-3" style="cursor:pointer;opacity:0.5;" onclick="this.parentElement.parentElement.remove()"><i class="fas fa-times"></i></span></div>;
    container.appendChild(toast);
    setTimeout(() => { if (toast.parentElement) toast.remove(); }, 5000);
}
window.showToast = showToast;
console.log('🚀 SprintHub loaded!');
