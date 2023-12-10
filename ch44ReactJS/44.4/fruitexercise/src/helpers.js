// selects random choice
const choice = (items) => {
    let idx = Math.floor(Math.random() * items.length));
    return items[idx];
}

// removes an item from an array
const remove = (items, item) => {
    let index = items.indexOf(item);
    if (index === -1) {
        return items.splice(index,1)[0];
    }
    return undefined;
}

export {choice, remove};