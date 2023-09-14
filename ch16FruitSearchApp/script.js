const input = document.querySelector('#fruit');
const suggestions = document.querySelector('.suggestions ul');

const fruit = ['Apple', 'Apricot', 'Avocado 🥑', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Currant', 'Cherry', 'Coconut', 'Cranberry', 'Cucumber', 'Custard apple', 'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava', 'Honeyberry', 'Huckleberry', 'Jabuticaba', 'Jackfruit', 'Jambul', 'Juniper berry', 'Kiwifruit', 'Kumquat', 'Lemon', 'Lime', 'Loquat', 'Longan', 'Lychee', 'Mango', 'Mangosteen', 'Marionberry', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon', 'Miracle fruit', 'Mulberry', 'Nectarine', 'Nance', 'Olive', 'Orange', 'Clementine', 'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear', 'Persimmon', 'Plantain', 'Plum', 'Pineapple', 'Pomegranate', 'Pomelo', 'Quince', 'Raspberry', 'Salmonberry', 'Rambutan', 'Redcurrant', 'Salak', 'Satsuma', 'Soursop', 'Star fruit', 'Strawberry', 'Tamarillo', 'Tamarind', 'Yuzu'];

function search(str, fruit) {
	let searchStr = str.toLowerCase();
	let results = [];
	for (let i = 0; i < fruit.length; i++) {
		let fruitStr = fruit[i].toLowerCase();
		if (fruitStr.includes(searchStr)) {
			results.push(fruit[i]);
		}
	}

	return results;
}






function searchHandler() {
	const list = document.querySelector('#list'); 

	input.addEventListener('input', function () {
		const typedText = input.value.trim();
		const results = search(typedText, fruit);

		// Clear older suggestions
		while (list.firstChild) {
			list.removeChild(list.firstChild);
		}

		// Remove list is input is empty
		if (!typedText) {
			return;
		}

		// Add new suggestions
		for (let i = 0; i < results.length; i++) {
			const newSuggestion = document.createElement('li');
			newSuggestion.setAttribute('class', 'choice');
			newSuggestion.textContent = results[i];
			list.appendChild(newSuggestion);

			// Add click event to populate textbox
			newSuggestion.addEventListener('click', function() {
				input.value = this.textContent;
			});
		}


	});


}

// Initialize the search handler
searchHandler();










input.addEventListener('keyup', searchHandler);
suggestions.addEventListener('click', useSuggestion);