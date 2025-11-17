document.addEventListener('DOMContentLoaded', function() {
  const addbtn = document.getElementById('add_item');
  const removeBtn = document.getElementById('remove_item');
  const clearBtn = document.getElementById('clear_list');
  const list = document.querySelector('.my_list');

  addbtn.addEventListener('click', function() {
	const newItem = document.createElement('li')
	newItem.textContent = 'Item';
	list.appendChild(newItem);
  });

  removeBtn.addEventListener('click', function() {
	if (list.lastElementChild) {
		list.removeChild(list.lastElementChild);
	}
  });

  clearBtn.addEventListener('click', function() {
	list.innerHTML = '';
  });
});