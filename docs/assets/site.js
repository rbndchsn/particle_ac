/* Progressive enhancement only: the site is fully readable without this file. */
(function () {
  "use strict";

  /* Table-of-contents scrollspy. */
  var links = Array.prototype.slice.call(
    document.querySelectorAll(".toc a, .home-rail .rail-block:first-child .rail-list a"));
  if (links.length && "IntersectionObserver" in window) {
    var byId = {};
    var targets = links.map(function (a) {
      var el = document.getElementById(a.getAttribute("href").slice(1));
      if (el) byId[el.id] = a;
      return el;
    }).filter(Boolean);

    var visible = new Set();
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) visible.add(e.target.id);
        else visible.delete(e.target.id);
      });
      var first = targets.find(function (t) { return visible.has(t.id); });
      links.forEach(function (a) { a.classList.remove("active"); });
      if (first && byId[first.id]) byId[first.id].classList.add("active");
    }, { rootMargin: "-72px 0px -70% 0px" });
    targets.forEach(function (t) { obs.observe(t); });
  }

  /* Claims-register filtering. */
  var bar = document.querySelector("[data-filter-table]");
  if (!bar) return;
  var table = bar.parentNode.querySelector("table");
  if (!table) return;
  var rows = Array.prototype.slice.call(table.querySelectorAll("tbody tr"));
  var countEl = bar.querySelector(".count");

  function apply(filter) {
    var shown = 0;
    rows.forEach(function (r) {
      var s = r.getAttribute("data-status");
      var show = filter === "all" || s === filter;
      r.hidden = !show;
      if (show && s) shown++;
    });
    if (countEl) {
      var total = rows.filter(function (r) { return r.getAttribute("data-status"); }).length;
      countEl.textContent = filter === "all"
        ? total + " claims" : shown + " of " + total + " claims";
    }
  }

  bar.addEventListener("click", function (e) {
    var btn = e.target.closest("button[data-f]");
    if (!btn) return;
    bar.querySelectorAll("button[data-f]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b === btn));
    });
    apply(btn.getAttribute("data-f"));
  });

  apply("all");
})();
