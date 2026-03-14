const pytest = require('pytest');
const config = require('../config');

pytest.describe('Config Tests', () => {
  pytest.it('should have light theme', () => {
    // Assert
    pytest.expect(config.theme.light).toBeDefined();
    pytest.expect(config.theme.light.background).toBe('#ffffff');
    pytest.expect(config.theme.light.text).toBe('#000000');
  });

  pytest.it('should have dark theme', () => {
    // Assert
    pytest.expect(config.theme.dark).toBeDefined();
    pytest.expect(config.theme.dark.background).toBe('#000000');
    pytest.expect(config.theme.dark.text).toBe('#ffffff');
  });

  pytest.it('should handle error when theme is not set', () => {
    // Arrange
    const config = {
      theme: null
    };

    // Act and Assert
    pytest.expect(() => config.theme.light).toThrowError();
  });
});