(function ($) {
  $(function () {
    const session_id = document.querySelector("#session-id").innerText;
    //console.log(session_id);

    let formData = new FormData();

    formData.append("obj_id", session_id);

    $.ajax({
      url: "/api/mypage",
      method: "POST",
      data: formData,
      dataType: "json",
      contentType: false,
      processData: false,
      success: function (data) {
        // 유저 정보

        const hidden = document.querySelector("#hidden");
        hidden.remove();

        let name = data["name"];
        let nick_name = data["nickname"];
        let email = data["email"];

        if (!nick_name) {
          nick_name = "머스크";
        }

        let createday = data["createday"]["$date"];
        let day = createday.substr(0, 10);

        let temp_html = `<div>
                            <h2>이름 : ${name}</h2>
                            <h2>닉네임 : ${nick_name}</h2>
                            <h2>이메일 : ${email}</h2>
                            <h2>계정생성일 : ${day}</h2>
                        </div>`;
        $("#userinfo-container").append(temp_html);

        // 유저가 업로드한 게시판 정보
      },
      error: function (error) {
        console.error(error);
      },
    });
  });
})(jQuery);
