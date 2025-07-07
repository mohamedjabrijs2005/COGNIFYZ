module.exports = {
  testEnvironment: 'node',
  collectCoverage: true,
  coverageDirectory: 'coverage',
  testMatch: ['**/src/**/*.test.ts'],
  transform: {
    '^.+\\.ts$': 'ts-jest',
  },
};