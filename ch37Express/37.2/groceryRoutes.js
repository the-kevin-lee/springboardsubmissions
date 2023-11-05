const express = require("express")
const router = new express.Router()
const items = require("./fakeDB")


// GET display all items
router.get('/', (req,res) =>{
    res.json(items);
})

// GET retrieve grocery item by name
router.get('/:name', (req,res) => {
    const item = items.find(i => i.name === req.params.name);
    if (!item) {
        return res.status(404).json({ error: 'Item not found' });
    }
    res.json(item);
})


// POST adding a new grocery item
router.post('/',(req,res) => {
    const {name,price} = req.body;
    const newItem = {name, price};
    items.push(newItem);
    res.status(201).json({added: newItem});
})

router.patch('/:name', (req,res) => {
    const {name} = req.params;
    const {newName, price} = req.body;
    const item = items.find(item => item.name === name);
    if (!item) {
        return res.status(404).json({message: "Item not found"});
    }   
    if (newName) item.name = newName;
    if (price) item.price = price;
    res.json({updated: item});
})

router.delete('/:name',(req,res) => {
    const {name} = req.params;
    const itemIndex = items.findIndex(item => item.name === name);
    if (itemIndex === -1) {
        return res.status(404).json({message: "Item not found"});
    }
    items.splice(itemIndex, 1);
    res.json({message: 'Deleted'});
})

// exporting router
module.exports = router;