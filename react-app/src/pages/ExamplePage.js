import React from 'react';
import { Button } from '@material-ui/core';

function testFlask() {
  fetch("/testflask").then(res => res.json()).then(data => {
    alert(JSON.stringify(data))
  });
}

function ExamplePage() {
	return (<>
		<img src="oportun_logo_circle.png" className="App-logo" alt="logo" />
        <Button
          variant="contained" color="primary"
          onClick={testFlask}>
            Test Button
        </Button>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
	</>);
}

export default ExamplePage;