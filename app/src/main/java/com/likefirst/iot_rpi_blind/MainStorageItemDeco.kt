package com.likefirst.iot_rpi_blind

import android.content.Context
import android.graphics.Rect
import androidx.recyclerview.widget.RecyclerView
import android.util.TypedValue
import android.view.View

class MainStorageItemDeco : RecyclerView.ItemDecoration() {
    var size10 : Int = 0
    var size5 : Int = 0

    fun initSize(context: Context) {
        size10 = dpToPx(context, 10)
        size5 = dpToPx(context, 5)
    }

    // dp -> pixel 단위로 변경
    private fun dpToPx(context: Context, dp: Int): Int {
        return TypedValue.applyDimension(
            TypedValue.COMPLEX_UNIT_DIP,
            dp.toFloat(),
            context.getResources().getDisplayMetrics()
        )
            .toInt()
    }

    override fun getItemOffsets(
        outRect: Rect,
        view: View,
        parent: RecyclerView,
        state: RecyclerView.State
    ) {
        super.getItemOffsets(outRect, view, parent, state)

        val position = parent.getChildAdapterPosition(view)
        val itemCount = state.itemCount

        outRect.right = size5
        outRect.bottom = size5
        outRect.left = size5
        outRect.bottom = size5

        if(itemCount.shr(1).and(1) == 0){   // 짝수일때
            when(position){
                0 -> {
                    outRect.top = size10
                    outRect.left = size10
                }
                1 -> {
                    outRect.top = size10
                    outRect.right = size10
                }
                itemCount-2 -> {
                    outRect.bottom = size10
                    outRect.left = size10
                }
                itemCount-1 -> {
                    outRect.bottom = size10
                    outRect.right = size10
                }
            }
        } else {    // 홀수 일 때
            when(position){
                0 -> {
                    outRect.top = size10
                    outRect.left = size10
                }
                1 -> {
                    outRect.top = size10
                    outRect.right = size10
                }
                itemCount-1 -> {
                    outRect.bottom = size10
                    outRect.left = size10
                }
            }
        }

    }
}