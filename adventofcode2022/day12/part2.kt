import java.io.File

const val DEBUG = true

/**
 * Use to debug code, a drop-in replacement for [println].
 *
 * It will only print if [DEBUG] is true.
 */
fun debug(contents: Any) {
    if (DEBUG) {
        println(contents)
    }
}

// In Kotlin, data classes are compared against one another by their values, and not their memory locations.
// No custom equals() method is needed.
data class Position
    (var x: Int, var y: Int)

class HeightMap(private val input: List<String>) {


    private fun produceNeighbours(pos: Position) =
        listOf<Position>(
            Position(pos.x, pos.y - 1),
            Position(pos.x - 1, pos.y),
            Position(pos.x + 1, pos.y),
            Position(pos.x, pos.y + 1)
        )

    private fun neighboursReachable(pos: Position): List<Position> {
        val neighbours = produceNeighbours(pos)
        var currentValue: Char = input[pos.y][pos.x]

        val reachablePositions = mutableListOf<Position>()


        for (neighbour in neighbours) {
            val yExist = !(neighbour.y >= input.size || neighbour.y < 0)
            // There should be at least one row and all rows are uniform in length. Hence, we take input[0]
            val xExist = !(neighbour.x >= input[0].length || neighbour.x < 0)
            if (yExist && xExist) {
                var value = input[neighbour.y][neighbour.x]
                if (value == 'E') {
                    value = 'z'
                }
                if (currentValue == 'E') {
                    currentValue = 'z'
                }
                val diff = value.code - currentValue.code
                debug("value $value current $currentValue")
                if ((diff >= -1) || currentValue == 'S') {
                    // can reach
                    reachablePositions.add(neighbour)
                }
            }

        }
        debug(reachablePositions)
        return reachablePositions.toList() // render immutable
    }

    private val queue = ArrayDeque<Pair<Position, Int>>()
    private val visited: MutableList<Position> = mutableListOf()
    private val stepMap: MutableMap<Position, Int> = mutableMapOf()

    fun calculate(start: Position): Int? {
        queue.addLast(Pair(start, 0))

        while (!queue.isEmpty()) {
            val item = queue.removeFirst()
            debug("current cost ${item.second} current posn ${item.first} value is ${input[item.first.y][item.first.x]}")

            if (item.first in visited) {
                debug("skipped")
                continue
            }
            visited.add(item.first)
            stepMap[item.first] = item.second
            if (input[item.first.y][item.first.x] == 'a') {
                return item.second
            }
            for (neighbour in neighboursReachable(item.first)) {
                if (neighbour !in visited) {
                    val neighbourSteps = item.second + 1
                    queue.addLast(Pair(neighbour, neighbourSteps))
                }
            }
        }
        return null
    }
}


fun main() {
    val lines = File("input").readLines()
    val heightMap = HeightMap(lines)

//    val start = Position(0, 20)
//    val end = Position(68, 20)


    val steps = heightMap.calculate(Position(68, 20))
    println("Steps: $steps")


}
