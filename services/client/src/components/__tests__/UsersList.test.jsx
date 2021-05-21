import React from 'react';
import renderer from 'react-test-renderer';
import { shallow } from 'enzyme';

import UsersList from '../UsersList';

const users = [
  {
    'active': true,
    'email': 'test1@example.com',
    'id': 1,
    'username': 'test1'
  },
  {
    'active': true,
    'email': 'test2@example.com',
    'id': 2,
    'username': 'test2'
  }
];

test('UsersList renders properly', () => {
  const wrapper = shallow(<UsersList users={users} />);
  const element = wrapper.find('h4');
  expect(element.length).toBe(2);
  expect(element.get(0).props.children).toBe('test1');
});

test('UsersList renders a snapshot properly', () => {
  const tree = renderer.create(<UsersList users={users}/>).toJSON();
  expect(tree).toMatchSnapshot();
});
