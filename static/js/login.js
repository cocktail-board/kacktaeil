// (function ($) {
//   $(function () {
//     alert("가나여~");
//   });
// })(jQuery);

function login() {
  let login_form = document.querySelector("#login-form");
  let formData = new FormData(login_form);

  $.ajax({
    type: "POST",
    url: "/api/login",
    data: formData,
    contentType: false,
    processData: false,
    success: function (data) {
      console.log("성공");
      const check = data["result"];
      if (check !== "success") {
        alert("로그인 실패");
        window.location.reload();
      }
      if (check === "success") {
        alert("로그인 성공");
        window.location.replace("/board");
      }
    },
    error: function (req, status, error) {
      console.log("ajax 에러임");
    },
  });
}
