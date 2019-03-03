<template>
  <div class="form-app">
    <div v-show="!isSubmit" class="section">
      <div class="logo"><img src="images/logo.png" width="180" srcset="images/logo-p-500.png 500w, images/logo-p-800.png 800w, images/logo-p-1080.png 1080w, images/logo.png 1270w" sizes="(max-width: 479px) 75vw, 180px" alt=""></div>
      <div class="hero-container w-container">
        <h1 class="h1">Bet a Macy's</h1>
        <h4><strong class="h3">Create a trackable bet with your friends for a Macy's product.</strong></h4>
      </div>
    </div>
    <div v-show="!isSubmit" class="primary-container w-container">
      <div class="w-form">
        <form id="email-form" name="email-form" data-name="Email Form">
          <div class="credentials"><img src="images/high-five-icon.svg" alt="" class="highfive-icon" data-ix="high-five-wiggle-repeat">
            <h3><strong class="h2">Create Your Contract Here</strong></h3>
            <div class="w-row">
              <div class="w-col w-col-5">
                <label for="your_name" class="field-label">Your Name</label>
                <input v-model="yourName" type="text" class="text-field w-input" maxlength="256" name="your_name" data-name="your_name" id="your_name" required="">
                <label for="your_email" class="field-label">Your Email</label>
                <input v-model="yourEmail" type="email" class="text-field w-input" maxlength="256" name="your_email" data-name="your_email" id="your_email" required=""></div>
              <div class="column w-col w-col-2"><img src="images/chevron-mobile-icon.svg" alt="" class="image">
                <img src="images/chevron-icon.svg" alt="" class="chevron"></div>
              <div class="w-col w-col-5">
                <label for="rec_name" class="field-label">Recipient&#x27;s Name</label>
                <input v-model="recName" type="text" class="text-field w-input" maxlength="256" name="rec_name" data-name="rec_name" id="rec_name" required="">
                <label for="rec_email" class="field-label">Recipient&#x27;s Email</label>
                <input v-model="recEmail" type="email" class="text-field w-input" maxlength="256" name="rec_email" data-name="rec_email" id="rec_email" required=""></div>
            </div>
            <div class="w-row">
              <div class="w-col w-col-5">
                <label for="your_name" class="field-label">Your Ethereum Address</label>
                <input v-model="eth_1" type="text" class="text-field w-input" maxlength="256" name="your_name" data-name="your_name" id="your_name" required="">
                </div>
              <div class="column w-col w-col-2"><img src="images/chevron-mobile-icon.svg" alt="" class="image">
               </div>
              <div class="w-col w-col-5">
                <label for="rec_name" id = "rec" class="field-label">Recipient&#x27;s Ethereum Address</label>
                <input v-model="eth_2" type="text" class="text-field w-input" maxlength="256" name="rec_name" data-name="rec_name" id="rec_name" required="">
                </div>
            </div>
          </div>
          <div class="separator"></div>
          <div class="contract-terms">
            <img src="images/message-icon.svg" alt="" class="chat-icon" data-ix="promise-wiggle-repeat">
            <h3><strong class="h2">What&#x27;s the bet about?</strong></h3>
            <textarea v-model="promise" id="promise" name="promise" placeholder="Enter the promise details here. Do not forget to add the punishment details for not following through!" maxlength="5000" data-name="promise" required="" class="textarea w-input"></textarea></div>
            <div class="separator"></div>
            <div class="contract-terms">
            <h3><strong class="h2">Enter the product ID</strong></h3>
            <textarea v-model="pid" id="pid" name="pid" placeholder="Enter the product ID of the Macy's product you wanna stake in the bet." maxlength="5000" data-name="pid" required="" class="textarea w-input"></textarea></div>
          <div class="separator"></div>
          <div><input v-on:click="sendEmail" id = "sub" type="submit" value="Submit" data-wait="Please wait..." class="submit-button w-button"></div>
        </form>
        <div v-show="isSuccess" class="w-form-done">
          <div>Thank you! Your submission has been received!</div>
        </div>
        <div v-show="isFail" class="w-form-fail">
          <div>Oops! Something went wrong while submitting the form.</div>
        </div>
      </div>
    </div>
    <div v-show="isSuccess" class="success-container w-container">
      <div>
        <div class="notification-icon-container"><img src="images/pinky-icon-notification.svg" alt="" class="highfive-icon" data-ix="high-five-wiggle-repeat"></div>
        <div class="centered">
          <h2 class="notifification-h1"><strong class="bold-text-2">Congratulations, your Betcy Contract has been submitted!</strong></h2>
          <div class="notification-paragraph"><strong class="bold-text-3">You and your recipient should receive an email with the bet that you have provided. Both of you need to click Agree to make the bet binding.</strong></div>
          <div></div>
        </div>
        <div class="centered">
          <h2 class="notifification-h1"><strong class="bold-text-2">The Macy's product that you have wagered is:</strong></h2>
          <div class="notification-paragraph"><strong class="bold-text-3"><a href="http://www1.macys.com/shop/product/givenchy-16-necklace-rose-gold-tone-crystal-fireball-pendant-necklace?ID=792565" target="blank">http://www1.macys.com/shop/product/givenchy-16-necklace-rose-gold-tone-crystal-fireball-pendant-necklace?ID=792565</a></strong></div>
          <div><button style="margin-top:24px;" v-on:click="showEmailPage" class="submit-button w-button">Next</button></div>
        </div>
      </div>
    </div>
    <div v-show="showEmail" class="email-container w-container">
      <div>
        <h3><strong class="email-h1">You Have a Betcy Request!</strong></h3>
        <div class="email-paragraph"><strong>Tanmay Agrawal</strong> and <strong>Souradeep Das</strong> have a Betcy pending for review. You can either Agree or Disagree. If both parties agree, your <strong>Betcy will become binding</strong> and a URL with your bet will be sent to both of you.</div>
      </div>
      <div class="promise-content">
        <h3><strong class="email-h1">The Betcy Terms:</strong></h3>
        <div class="email-paragraph"><strong class="bold-text-4">&quot;I, Tanmay Agrawal, agree to participate in a "Betcy" between myself and Souradeep Das.&quot;</strong></div>
      </div>
      <div class="div-block-2">
        <h3><strong class="email-h1">What is your decision?</strong></h3>
        <div><strong class="email-paragraph">This action cannot be undone. Choose wisely.</strong></div><a v-on:click="showAcceptedPage" href="#" class="email-accept-button w-button">I Agree</a><a href="#" class="email-reject-button w-button">I Disagree</a></div>
    </div>
    <div v-show="showAccepted" class="email-container w-container">
      <div>
        <h3><strong class="email-h1">The Betcy Has Been Accepted by Both Parties.</strong></h3>
        <div class="email-paragraph">Both<strong> Tanmay Agrawal</strong> and <strong>Souradeep Das</strong> have agreed to the following Betcy terms:</div>
      </div>
      <div class="promise-success">
        <h3><strong class="email-h1">The Betcy Terms:</strong></h3>
        <div class="email-paragraph"><strong class="bold-text-4">&quot;I, Tanmay Agrawal, agree to participate in a "Betcy" between myself and Souradeep Das.&quot;</strong></div>
      </div>
      <div class="div-block-2">
        <h3><strong class="email-h1">Here Is Your Unique Betcy URL: </strong></h3>
        <div><strong class="email-paragraph">This URL is permanently stored on an Ethereum Blockchain and you can come back to it whenever you want.</strong></div>
        <div class="div-block-4"><a href="#" class="link">www.betcy.com/3G5HD3H1</a></div>
      </div>
      <div class="div-block-3">
        <div class="email-paragraph"><strong class="hash-itself">0xF97813d9788F742ccEA5c113259f81E70c09D7B8</strong></div>
      </div>
    </div>
  </div>
</template>

    <script>
      var getProductID = {
               "async": true,
               "crossDomain": true,
               "url": "https://www.jsonstore.io/cc18fd5358601223f518adc547cb765a84d85d34fbdfe3466b55d6e454f29bf1",
               "method": "GET"
               };

             $.ajax(getProductID).done(function (response) {
               var prod = JSON.stringify(response);
               // console.log(JSON.stringify(response));
                 console.log(response.result);
               });

             var setProductID = {
                "async": true,
                "crossDomain": true,
                "url": "https://api.macys.com/v4/catalog/product/77589%28productdetails%28summary%29%29?productID=%2077589,520910&productdetails=%28productdetails%28price,summary%29%29",
                "method": "GET",
                "headers": {
                  "Accept": "application/json",
                  "x-macys-webservice-client-id": "h4ckathon",
                  "cache-control": "no-cache",
                  "Postman-Token": "40d0cb4e-dcf1-4cc0-92de-39649ddebfb0",
                  "Access-Control-Allow-Origin": 'http://10.142.8.181:8081/'
                }
              };

              $.ajax(setProductID).done(function (response) {
                var prod = JSON.stringify(response);
                // console.log(JSON.stringify(response));
                  console.log(response.product[0].id);
                });

</script>
<script>
  import axios from 'axios'
export default {
  name: 'Form',
  data: function() {
    return {
      showAccepted: false,
      showEmail: false,
      isSubmit: false,
      isSuccess: false,
      isFail: false,
      yourName: 'Tanmay Agrawal',
      yourEmail: 'tanmayagrawal@berkeley.edu',
      recName: 'Souradeep Das',
      recEmail: 'souradeep@berkeley.com',
      promise: 'I, Tanmay Agrawal, agree to participate in a "Betcy" between myself and Souradeep Das.',
      pid: '792565',
      eth_1: '0xD91f848796e092De699C535f8eD72024Af079372',
      eth_2: '0xAcb7e46EA96A1C39C1eaF160FBACD302B3F28e17',
    }
  },
  mounted() {
    window.Webflow.require('ix').init([
      {"slug":"high-five-wiggle","name":"high-five-wiggle","value":{"style":{"title":"empty","opacity":0,"x":"0px","y":"0px","z":"0px"},"triggers":[{"type":"load","stepsA":[{"opacity":1,"transition":"opacity 250ms ease-out 0, transform 200 ease 0","rotateX":"0deg","rotateY":"0deg","rotateZ":"27deg"},{"transition":"transform 250ms ease-out 0","rotateX":"0deg","rotateY":"0deg","rotateZ":"-30deg"},{"opacity":1,"transition":"transform 250ms ease-out 0, opacity 200 ease 0","rotateX":"0deg","rotateY":"0deg","rotateZ":"3deg"}],"stepsB":[]}]}},
      {"slug":"high-five-wiggle-repeat","name":"high-five-wiggle-repeat","value":{"style":{"title":"empty","opacity":0,"x":"0px","y":"0px","z":"0px"},"triggers":[{"type":"load","loopA":true,"stepsA":[{"opacity":1,"transition":"opacity 250ms ease-out 0, transform 300ms ease-out-back 0","rotateX":"0deg","rotateY":"0deg","rotateZ":"5deg"},{"transition":"transform 300ms ease-out-back 0","rotateX":"0deg","rotateY":"0deg","rotateZ":"-5deg"}],"stepsB":[]}]}},
      {"slug":"promise-wiggle-repeat","name":"promise-wiggle-repeat","value":{"style":{"title":"empty","opacity":0,"x":"0px","y":"0px","z":"0px"},"triggers":[{"type":"load","loopA":true,"stepsA":[{"opacity":1,"transition":"opacity 250ms ease-out 0, transform 300ms ease-out-back 0","rotateX":"0deg","rotateY":"0deg","rotateZ":"-5deg"},{"transition":"transform 300ms ease-out-back 0","rotateX":"0deg","rotateY":"0deg","rotateZ":"5deg"}],"stepsB":[]}]}},
      {"slug":"zoom-and-scale","name":"Zoom and scale","value":{"style":{"opacity":0,"scaleX":0.69,"scaleY":0.69,"scaleZ":1},"triggers":[{"type":"load","stepsA":[{"opacity":1,"transition":"transform 250ms ease-out-back 0, opacity 200 ease 0","scaleX":1,"scaleY":1,"scaleZ":1}],"stepsB":[]}]}}
    ]);
  },
  methods: {
    sendEmail() {
      event.preventDefault()
      this.isSubmit = true;
      let self = this;
      // let url = 'https://api.pinkypromisecompany.com/register';
      let url = 'https://api.pinkypromisecompany.com/register';
      $.post(url, {
        your_name: this.yourName,
        your_email: this.yourEmail,
        rec_name: this.recName,
        rec_email: this.recEmail,
        promise: this.promise
      }, function(data, status) {
        self.isSuccess = true;
        window.get_results()
        console.log(data)
        console.log(status)
      })

    },
    showEmailPage() {
      this.isSuccess = false
      this.showEmail = true
    },
    showAcceptedPage() {
      this.showEmail = false;
      this.showAccepted = true;
    }
  }
}

// async function get_results() {
//   let user2="535353"
//   let email1="dhgdhg@fd.com"
//   let email2="dgydgd@.com"
//   let message="dfdhdg"
//   await contract.createPinky({user2:user2, email1: email1, email2: email2, message: message})
//   let bytes=await contract.showPinky({sender: accountId})
//   return bytes
// }

</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
