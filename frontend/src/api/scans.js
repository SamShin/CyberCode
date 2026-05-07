/**
 * API scan endpoints.
 * Handles creating, retrieving, and exporting scan results.
 */

export const createScan = async (scanData) => {
  // Call POST /scans to create new scan
  return null
}

export const getScan = async (scanId) => {
  // Call GET /scans/{scanId} to retrieve scan details
  return null
}

export const listScans = async (limit = 10) => {
  // Call GET /scans to list user's scans
  return null
}

export const deleteScan = async (scanId) => {
  // Call DELETE /scans/{scanId} to delete a scan
  return null
}

export const exportScan = async (scanId, format = 'json') => {
  // Call GET /scans/{scanId}/export?format={format} to export results
  return null
}
