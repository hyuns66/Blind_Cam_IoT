package com.likefirst.iot_rpi_blind

import android.annotation.SuppressLint
import android.content.Context
import android.net.Uri
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.google.firebase.storage.StorageReference
import com.likefirst.iot_rpi_blind.databinding.ItemStorageRvBinding

class MainStorageRVAdapter(val imgList : List<StorageReference>, val context: Context) : RecyclerView.Adapter<MainStorageRVAdapter.ViewHolder>() {

    lateinit var mItemClickListener : ItemClickListener

    interface ItemClickListener{
        fun gotoGallery(position: Int)
    }

    fun setClickListener(itemClickListener : ItemClickListener){
        mItemClickListener = itemClickListener
    }

    inner class ViewHolder(val binding : ItemStorageRvBinding, val context : Context) : RecyclerView.ViewHolder(binding.root) {
        fun init(position : Int){   // imgList에 있는 각각의 사진정보를 download 한 뒤 glide로 바인딩해준다.
            imgList[position].downloadUrl.addOnSuccessListener { it ->
                Glide.with(context)
                    .load(it)
                    .override(150, 150)
                    .into(binding.firebaseIv)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MainStorageRVAdapter.ViewHolder {
        val binding = ItemStorageRvBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding, parent.context)
    }

    override fun getItemCount(): Int {
        return imgList.size
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.init(position)
        holder.itemView.setOnClickListener {
            mItemClickListener.gotoGallery(position)
        }

        // preload
//        if(position < itemCount){
//            val endposition = if(position+12 >= itemCount-1){
//                itemCount-1
//            } else {
//                position+12
//            }
//
//            imgList.subList(position, endposition).forEach {
//                it.downloadUrl.addOnSuccessListener {
//                    preload(context, it)
//                }
//            }
//        }
    }

//    fun preload(context: Context,  url : Uri) {
//        Glide.with(context).load(url)
//            .preload(150, 150)
//    }
}