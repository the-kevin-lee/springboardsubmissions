
it('should calculate the monthly rate correctly', function () {
  
  const factors1 = {
    principal: 30000,
    years: 10,
    rate: 6
  }
  const factors2 = {
    principal: 10000,
    years: 5,
    rate: 4
  }
  expect(update(factors1).toEqual('333.06'));
  expect(update(factors2).toEqual('184.17'));
});


it("should return a result with 2 decimal places", function() {
  const factors 3 = {
    principal: 10043,
    years: 8,
    rate: 5.8
  }
  expect(update(factors3).toEqual('131.00'));
});

