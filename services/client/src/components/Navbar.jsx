import React from 'react';
import { makeStyles } from '@material-ui/core'
import {CssBaseline } from '@material-ui/core';
import { AppBar } from '@material-ui/core';
import { Toolbar } from '@material-ui/core';
import { Typography } from '@material-ui/core';
import { Button } from '@material-ui/core';
import { Redirect, useHistory } from 'react-router';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  title: {
    flexGrow: 1,
    display: 'block',
  },
}));

const Navbar = () => {
  const classes = useStyles();
  const history = useHistory();

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position="static">
        <Toolbar>
          <Typography className={classes.title} variant="h6">
            Wadizu
          </Typography>
          <Button color="inherit" onClick={() => {
            history.push('/login')
          }}>Sign in</Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default Navbar;