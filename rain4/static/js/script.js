(function () {
  const texts = [
    "User-friendly — clear inputs, instant feedback, minimal steps.",
    "On-spot assessment — estimate harvest potential by location and roof area.",
    "Feasibility analysis — suggested recharge types and structural sizing.",
    "Cost & benefit — quick estimates to support decision-making."
  ];
  const slideTextEl = document.getElementById("slideText");
  let idx = 0;
  const intervalMs = 3000;
  const fadeDuration = 620;

  function showNext() {
    slideTextEl.style.opacity = 0;
    setTimeout(() => {
      idx = (idx + 1) % texts.length;
      slideTextEl.innerText = texts[idx];
      slideTextEl.style.opacity = 1;
    }, fadeDuration);
  }
  setInterval(showNext, intervalMs);
})();
