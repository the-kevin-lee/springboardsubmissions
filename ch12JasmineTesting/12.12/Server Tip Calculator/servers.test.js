// Test suite for server-related functionality
describe("Servers test (with setup and tear-down)", function() {
  // Runs before each individual test within this describe block
  beforeEach(function () {
    // Initialization logic: setting the value of serverNameInput to 'Alice'
    serverNameInput.value = 'Alice';
  });

  // Individual test case
  it('should add a new server to allServers on submitServerInfo()', function () {
    // Calling the function to be tested
    submitServerInfo();

    // Expectation: Checking that there is exactly one server in allServers
    expect(Object.keys(allServers).length).toEqual(1);
    // Expectation: Checking that the server's name is 'Alice'
    expect(allServers['server' + serverId].serverName).toEqual('');
  });

  it('should not add a new server with an empty string' function() {
    serverNameInput.value = '';
    submitServerInfo();
    expect(Object.keys(allServers).length.toEqaul(0));
  })

  it('should update #servertable upon updateServerTable()' function() {
    submitServerInfo();
    updateServerTable();

    let TdList = document.querySelectorAll('#serverTable tbody tr td');

expect(TdList.length).toEqaul(3);
expect(TdList[0].innerText).toEqaul('Alice');
expect(TdList[1].innerText).toEqaul('$0.00');


  })

  // Runs after each individual test within this describe block
  afterEach(function() {
    serverId = 0;
    serverTbody.innerHTML = '';
    allServers = {};

  });
});

