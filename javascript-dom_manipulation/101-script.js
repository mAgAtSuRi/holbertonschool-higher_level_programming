document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('btn_translate');
  const select = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  btn.addEventListener('click', function () {
    const lang = select.value;

    if (!lang) {
      helloDiv.textContent = 'Please choose a language.';
      return;
    }

    const url = `https://hellosalut.stefanbohacek.com/?lang=${lang}`;

    fetch(url)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error:', error);
        helloDiv.textContent = 'Error fetching translation.';
      });
  });
});
