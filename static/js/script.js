$(document).ready(function () {
  // Change user
  $(".user").click(function () {
    let currUser = $(this).find(".name").text();
    let currUserImg = $(this).find("img").attr("src");
    $(".msg-area-header").find("img").attr("src", currUserImg);
    $(".msg-area-header").find(".name").text(currUser);
    // Clearing Message area
    $(".msg-content").text("");
  });
  // message from input
  $(".texting").submit(false);

});

// messege container to send and recive message
function sendMessage(msg) {
  let newMessage = document.createElement("div");
  newMessage.setAttribute("class", "d-flex justify-content-end");
  newMessage.style.marginBottom = "23px";
  // margin-right: 612px;
  newMessage.innerHTML = `
    <div class="my-msg rounded-pill text-white text-right bg-primary">
        ${msg}
    </div>
  `;
  return newMessage;
}

function recvMessage(msg) {
  let newMessage = document.createElement("div");
  newMessage.setAttribute("class", "d-flex justify-content-start");
  newMessage.innerHTML = `
  <div class="other-msg rounded-pill text-dark bg-white">
    ${msg}
  </div>
  `;
  return newMessage;
}
