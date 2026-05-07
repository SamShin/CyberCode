/**
 * ScanCard component - displays summary of a single scan.
 */
export default function ScanCard({ scan }) {
  return (
    <div className="scan-card border rounded p-4">
      Scan Card: {scan && scan.name}
    </div>
  )
}
