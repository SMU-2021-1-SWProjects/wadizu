import React from 'react';
import { makeStyles } from '@material-ui/core';
import { Container } from '@material-ui/core';
import { Typography } from '@material-ui/core';

import Navbar from 'components/Navbar';

const useStyles = makeStyles((theme) => ({
  container: {
    margin: '100px auto 100px auto',
  },
  typography: {
    margin: '30px 0 30px 0',
  },
}));

const About = () => {
  const classes = useStyles();

  return (
    <div>
      <Navbar />
      <Container className={classes.container}>
        <Typography className={classes.typography} variant="h2" align="center">
          About
        </Typography>
        <Typography className={classes.typography} variant="h5" align="center">
          p0cka
        </Typography>
        <Typography className={classes.typography} variant="h6" align="center">
          PM Shane Oh<br/>
          TM Jongmin Park<br/>
          TM Jaesung Choi<br/>
          TM Sunheok Kim<br/>
          TM Taehyeon Ahn
        </Typography>
      </Container>
    </div>
  );
}

export default About;