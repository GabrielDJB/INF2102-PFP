import { render, screen } from '@testing-library/react';
import FocusChatApp from './FocusChatApp';

test('renders learn react link', () => {
  render(<FocusChatApp />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
