import { render, screen } from '@testing-library/react';
import App from './App';
import { MemoryRouter } from 'react-router-dom';
jest.mock('react-router-dom', () => ({
  Link: ({children}) => <div>{children}</div>,
  Routes: ({children}) => <div>{children}</div>,
  Route: () => null,
  MemoryRouter: ({children}) => <div>{children}</div>
}));

test('renders header', () => {
  render(
    <MemoryRouter>
      <App />
    </MemoryRouter>
  );
  const heading = screen.getByText(/Fuyu App/i);
  expect(heading).toBeInTheDocument();
});
