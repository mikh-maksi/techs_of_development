k = 1;
query = 'https://innovations.kh.ua/quiz/list/?author_id=3&n='+k;
  console.log(query);
  fetch(query).then(response => response.json())
  .then(function (quiz) {
      console.log(quiz);
  })
