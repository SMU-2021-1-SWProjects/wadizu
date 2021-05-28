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

const Home = () => {
  const classes = useStyles();

  return (
    <div>
      <Navbar />
      <Container className={classes.container}>
        <Typography className={classes.typography} variant="h2" align="center">
          Welcome.
        </Typography>
        <Typography className={classes.typography} variant="h5" align="center">
          Wadizu is an openAPI.
        </Typography>
      </Container>
    </div>
  );
}

export default Home;