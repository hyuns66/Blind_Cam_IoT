package com.likefirst.iot_rpi_blind

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.RecyclerView
import androidx.viewpager2.adapter.FragmentStateAdapter
import com.bumptech.glide.Glide
import com.google.firebase.storage.StorageReference
import com.likefirst.iot_rpi_blind.databinding.ItemGalleryVpBinding

class GalleryVpAdapter(val imgList : List<StorageReference>) : RecyclerView.Adapter<GalleryVpAdapter.ViewHolder>() {
    inner class ViewHolder(val binding : ItemGalleryVpBinding, val context : Context) : RecyclerView.ViewHolder(binding.root){
        fun initView(position: Int){
            imgList[position].downloadUrl.addOnSuccessListener { it ->
                Glide.with(context).load(it).into(binding.itemGalleryIv)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemGalleryVpBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding, parent.context)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.initView(position)
    }

    override fun getItemCount(): Int {
        return imgList.size
    }

}