/**
 * FindingRow component - displays a single security finding in a table row.
 */
export default function FindingRow({ finding }) {
  return (
    <tr className="finding-row">
      <td>Finding: {finding && finding.id}</td>
    </tr>
  )
}
