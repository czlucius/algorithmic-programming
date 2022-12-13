import java.io.File
import java.util.*
import java.util.regex.Matcher
import java.util.regex.Pattern

fun main() {
    val lines = File("input").readLines()
    val stacks = mutableListOf<ArrayDeque<String>>()
    var noOfColumns: Int = 0
    var maxNoOfRows: Int = 0

    for (line in lines) {
        if (line.startsWith(" 1   2")) {
            // The line we need for the number of columns.
            noOfColumns = line[line.length - 1].toString().toInt()
            break
        }
        maxNoOfRows++
    }

    for (col in (0 until noOfColumns)) {
        stacks.add(ArrayDeque(3))
    }

    var initialised = false

    var linenum = 0
    for (line in lines) {
        linenum++
        if (!line.startsWith(" 1   2")) {
            for (i in 0 until noOfColumns) {
                val num = i + 1
                val access = num + 3 * (num - 1)
                if (line[access] != ' ') {
                    stacks[i].add(line[access].toString())
                }
            }

        } else {
            break
        }
    }


    for (num in linenum until lines.size) {
        val pattern: Pattern = Pattern.compile("move ([0-9]+) from ([0-9]+) to ([0-9]+)")
        val matcher: Matcher = pattern.matcher(lines[num])
        if (matcher.find()) {
            val numToMove = matcher.group(1).toInt()
            val mvFrom = matcher.group(2).toInt()
            val mvTo = matcher.group(3).toInt()
            for (move in 0 until numToMove) {

                val temp = stacks[mvFrom-1].pop()
                stacks[mvTo-1].push(temp)
            }
        }
    }
    for (stack in stacks) {
        print(stack.peek())
    }


}