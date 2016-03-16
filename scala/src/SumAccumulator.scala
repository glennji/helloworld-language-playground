/**
 * Created by gmason on 27/05/15.
 */
class SumAccumulator {
  private var sum = 0
  def add(b: Byte) = { sum += b}
  def summation(): Int = { ~(sum & 0xFF) + 1}
}
