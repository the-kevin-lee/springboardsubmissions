const request = require('supertest');
const express = require('express');
const router = require('./groceryRoutes'); // adjust the path to your routes file

const app = express();
app.use(express.json());
app.use('/grocery', router);

describe('Grocery Routes', () => {

    //set up and tear down per test
    beforeEach(async() => {
        items.length = 0;
        await request(app)
            .post('/grocery')
            .send({name: 'Apple', price: 1.5});
    })



    it('should add a new item', async () => {
        const res = await request(app)
            .post('/grocery')
            .send({ name: 'Apple', price: 1.5 });
        expect(res.statusCode).toEqual(201);
        expect(res.body.added).toHaveProperty('name', 'Apple');
    });

    it('should update an item', async () => {
        const res = await request(app)
            .patch('/grocery/Apple')
            .send({ newName: 'Banana', price: 2 });
        expect(res.statusCode).toEqual(200);
        expect(res.body.updated).toHaveProperty('name', 'Banana');
    });

    it('should delete an item', async () => {
        const res = await request(app)
            .delete('/grocery/Banana');
        expect(res.statusCode).toEqual(404);
        expect(res.body).toHaveProperty('message', 'Deleted');
    });

    it('should get an item by name', async () => {
        const res = await request(app)
            .get('/grocery/Apple');
        expect(res.statusCode).toEqual(200);
        expect(res.body).toHaveProperty('name', 'Apple');
    });
});