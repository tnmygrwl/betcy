let initPromise;
window.initContract = function () {
  if (window.contract) {
    return Promise.resolve();
  }
  if (!initPromise) {
    initPromise = doInitContract();
  }
  return initPromise;
}

async function doInitContract() {
  const config = await nearlib.dev.getConfig();
  console.log("nearConfig", config);

  window.near = await nearlib.dev.connect();

  window.contract = await near.loadContract(config.contractName, {
    viewMethods: ["getMessages", "showPinky"],
    changeMethods: ["addMessage", "createPinky"],
    sender: nearlib.dev.myAccountId, //accountId
  });
}

function sleep(time) {
  return new Promise(function (resolve, reject) {
    setTimeout(resolve, time);
  });
}

window.get_results = async function() {
  let user2="Carra Llarm"
  let email1="felix_cited@mailinator.com"
  let email2="carra_llarm@mailinator.com"
  let message="I, Felix Cited, hereby promise to refer to Carra Llarm in puns for the next two weeks starting on the day of February 28, 2019"
  await window.contract.createPinky({user2:user2, email1: email1, email2: email2, message: message})
  let bytes=await window.contract.showPinky({sender: nearlib.dev.myAccountId})
  return bytes
}

initContract().catch(console.error);