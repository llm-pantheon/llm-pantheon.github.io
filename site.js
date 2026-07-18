// Pantheon site chrome — progressive enhancement only; the site works without JS.
// Upgrades the nav "copy as markdown" link: click copies the page's markdown twin
// to the clipboard instead of navigating. Plain link (and crawlers) unaffected.
(function () {
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  ready(function () {
    var link = document.querySelector('nav a.mdnav');
    if (!link || !navigator.clipboard || !window.fetch) return;
    var idle = link.textContent;
    link.addEventListener('click', function (e) {
      e.preventDefault();
      fetch(link.getAttribute('href'))
        .then(function (r) { if (!r.ok) throw 0; return r.text(); })
        .then(function (t) { return navigator.clipboard.writeText(t); })
        .then(function () {
          link.textContent = 'copied ✓';
          setTimeout(function () { link.textContent = idle; }, 1600);
        })
        .catch(function () { location.href = link.getAttribute('href'); });
    });
  });
})();
