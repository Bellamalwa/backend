const express = require('express');
const app = express();
const axios = require('axios');
const moment = require('moment');

app.get('/', (req, res) => {
  const slackName = req.query.slackName;
  const track = req.query.track;
  const utcTimeStamp = moment().utc().format("YYYY-MM-DDTHH:mm:ssZ");

  const data = {
    slack_name: slackName,
    current_day: new Date().getDay(),
    utc_time: utcTimeStamp,
    track: track,
    github_file_url: 'https://github.com/Bellamalwa/backend/blob/main/endpoint.js',
    github_repo_url: 'https://github.com/Bellamalwa/backend',
    status_code: 200
  };

  res.json(data);
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});