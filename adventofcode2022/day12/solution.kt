/**
  * WORK IN PROGRESS!
  */
import java.io.File
import java.lang.Exception
import java.lang.IndexOutOfBoundsException
const val DEBUG = true

fun debug(contents: Any) {
    if (DEBUG) {
        println(contents)
    }
}

data class Position
    (var x: Int, var y: Int)

class HeightMap(val input: List<String>) {
    private fun surroundingPositions(pos: Position) =
        listOf<Position>(
            Position(pos.x, pos.y - 1),
            Position(pos.x - 1, pos.y),
            Position(pos.x + 1, pos.y),
            Position(pos.x, pos.y + 1)
        )

    fun surroundingReachable(pos: Position): List<Position> {
        val surroundings = surroundingPositions(pos)
        val currentValue: Char = input[pos.y][pos.x]

        val reachablePositions = mutableListOf<Position>()


        for (cpos in surroundings) {
            print("cpos is $cpos")
            try {

                val value = input[cpos.y][cpos.x]
                val diff = value.code - currentValue.code
//                debug("value $value current $currentValue")
                debug("value is $value")
                if ((diff <= 1 ) || currentValue == 'S' || value == 'E') {
                    // can reach
                    reachablePositions.add(cpos)
                }
            } catch (_: IndexOutOfBoundsException) {
//                debug("Position x:${position.x}, y:${position.y} is not available")
            }
        }
//        debug("reachable posns $reachablePositions")
        return reachablePositions.toList() // render immutable
    }
    val queue = ArrayDeque<Pair<Position, Int>>()
    val visited: MutableList<Position> = mutableListOf()
    val stepMap: MutableMap<Position, Int> =mutableMapOf()
    fun calculate (start:Position, end:Position ): MutableMap<Position, Int> {
        queue.addLast(Pair(start, 1))

        while (!queue.isEmpty()) {
            val item = queue.removeFirst()
            debug("current cost ${item.second} current posn ${item.first}")

            if (item.first in visited) {
                debug("skipped")
                continue
            }
            visited.add(item.first)
            stepMap[item.first] = item.second
            if (item.first == end) {
                println("reach end! cost is ${item.second}")
                break
            }
            for (neighbour in surroundingReachable(item.first)) {
                if (neighbour !in visited){
                    val stepsN = item.second + 1
                    queue.addLast(Pair(neighbour, stepsN))
                }
            }
        }
        return stepMap
    }
}



fun main(args: Array<String>) {
    val lines = File("input").readLines()
    println(lines[20][68])
    val start = Position(0,20)

    val heightMap = HeightMap(lines)

    val steps = (heightMap.calculate(start, Position(68, 20)))
    // println("Steps: $steps")



}
