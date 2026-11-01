/* Vermont Junk — nav, attribution capture & conversion tracking.
 *
 * Why this matters (from the Google Ads review): Google was only counting
 * calls made directly from ads. Visitors who click through and then call
 * or fill out the form from the WEBSITE weren't being measured. This file
 * fires a conversion for every website call tap, text tap and form submit,
 * and stores the gclid so booked jobs can later be uploaded back to Google
 * Ads as offline conversions (optimizing on real customers, not just calls).
 */
(function () {
  var T = window.VJ_TRACKING || {};
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Mobile nav
  var toggle = document.querySelector(".nav-toggle"), nav = document.getElementById("nav");
  if (toggle && nav) toggle.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  // Capture attribution (gclid / utm) on landing — kept 90 days, matching Google's click window
  var params = new URLSearchParams(location.search);
  var keys = ["gclid", "gbraid", "wbraid", "utm_source", "utm_medium", "utm_campaign", "utm_term"];
  var now = Date.now();
  keys.forEach(function (k) { var v = params.get(k); if (v) { store.set("vj_" + k, v); store.set("vj_ts", String(now)); } });
  if (!store.get("vj_landing")) store.set("vj_landing", location.pathname);
  var ts = parseInt(store.get("vj_ts") || "0", 10);
  var fresh = ts && now - ts < 90 * 864e5;

  document.querySelectorAll("form[data-track-form]").forEach(function (f) {
    if (fresh) keys.forEach(function (k) {
      var input = f.querySelector('[name="' + k + '"]'); var v = store.get("vj_" + k);
      if (input && v) input.value = v;
    });
    var gclidInput = f.querySelector('[name="gclid"]');
    if (gclidInput && !gclidInput.value && fresh) gclidInput.value = store.get("vj_gbraid") || store.get("vj_wbraid") || "";
    var lp = f.querySelector('[name="landing_page"]'); if (lp) lp.value = store.get("vj_landing") || location.pathname;
    f.addEventListener("submit", function () { fire("generate_lead", { method: "form", where: f.dataset.trackForm }, T.ads_form_label); });
  });

  function fire(event, data, adsLabel) {
    data = data || {};
    data.page = location.pathname;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({ event: event }, data));
    if (typeof window.gtag === "function") {
      window.gtag("event", event, data);
      if (T.google_ads_id && adsLabel) window.gtag("event", "conversion", { send_to: T.google_ads_id + "/" + adsLabel });
    }
    if (typeof window.fbq === "function") window.fbq("track", event === "generate_lead" ? "Lead" : "Contact");
  }

  // Click-to-call & text tracking
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("[data-track]");
    if (!a) return;
    var kind = a.dataset.track;
    fire(kind === "call" ? "phone_call_click" : "text_click", { method: kind, where: a.dataset.where || "" },
      kind === "call" ? T.ads_call_label : null);
  });
})();
