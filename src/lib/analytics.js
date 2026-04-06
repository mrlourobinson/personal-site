// Google Analytics helper for SvelteKit
export const pageview = (url) => {
  if (typeof window.gtag !== 'undefined') {
    window.gtag('config', 'G-EB08QLL0S1', {
      page_path: url,
    });
  }
};

export const event = ({ action, category, label, value }) => {
  if (typeof window.gtag !== 'undefined') {
    window.gtag('event', action, {
      event_category: category,
      event_label: label,
      value: value,
    });
  }
};
