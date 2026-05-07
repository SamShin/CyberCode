/**
 * ReportViewer component - displays formatted scan report with findings.
 */
export default function ReportViewer({ report }) {
  return (
    <div className="report-viewer">
      Report Viewer - {report && report.scanId}
    </div>
  )
}
