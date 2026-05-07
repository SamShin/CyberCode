/**
 * API authentication endpoints.
 * Handles user login, registration, token refresh, and logout.
 */

export const login = async (email, password) => {
  // Call POST /auth/login with email and password
  return null
}

export const register = async (email, password, passwordConfirm) => {
  // Call POST /auth/register with email and passwords
  return null
}

export const refreshToken = async () => {
  // Call POST /auth/refresh to get new access token
  return null
}

export const logout = async () => {
  // Call POST /auth/logout to invalidate token
  return null
}
